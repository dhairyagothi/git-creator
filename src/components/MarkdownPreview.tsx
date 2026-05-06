import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import rehypeRaw from "rehype-raw";

export function MarkdownPreview({ source }: { source: string }) {
  return (
    <div className="prose-readme">
      <ReactMarkdown
        remarkPlugins={[remarkGfm]}
        rehypePlugins={[rehypeRaw]}
        urlTransform={(value: string) => value}
        components={{
          td: ({ node, ...props }) => {
            const nextProps: Record<string, unknown> = { ...props };
            if ("vAlign" in nextProps) {
              nextProps.valign = nextProps.vAlign as string;
              delete nextProps.vAlign;
            }
            return <td {...nextProps} />;
          },
          th: ({ node, ...props }) => {
            const nextProps: Record<string, unknown> = { ...props };
            if ("vAlign" in nextProps) {
              nextProps.valign = nextProps.vAlign as string;
              delete nextProps.vAlign;
            }
            return <th {...nextProps} />;
          },
          ...["div", "p", "h1", "h2", "h3"].reduce((acc, tag) => {
            acc[tag as keyof JSX.IntrinsicElements] = ({ node, ...props }: any) => {
              const nextProps: Record<string, any> = { ...props };
              if ("align" in nextProps) {
                nextProps.style = { ...nextProps.style, textAlign: nextProps.align };
                delete nextProps.align;
              }
              const Tag = tag as any;
              return <Tag {...nextProps} />;
            };
            return acc;
          }, {} as Record<string, React.ElementType>),
        }}
      >
        {source}
      </ReactMarkdown>
    </div>
  );
}
